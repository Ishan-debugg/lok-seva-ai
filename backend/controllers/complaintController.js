const axios = require("axios");
const pool = require("../config/db");

const departmentMap = {
  road: "Road & Traffic management Department",
  garbage: "Solid Waste Management",
  streetlight: "Electric Department",
  water: "Water Supply Department",
  sewage: "Sewage & Drainage Department",
  encroachment: "Encroachment Department"
};

const urgentWords = ["urgent", "immediately", "asap", "जल्दी", "तुरंत"];

function getPriority(text) {
  const lowerText = text.toLowerCase();
  return urgentWords.some(word => lowerText.includes(word)) ? "high" : "medium";
}

const stopWords = new Set(["is","a","an","the","on","in","at","near","to","for","of","and","or","with","here","there","this","that","these","those","it","its","by","from","up","about","into","over","after","before","out","off","down","no","not"]);

function getTokens(str) {
  if (!str) return [];
  return str.toLowerCase()
    .replace(/[^a-z0-9\s\u0900-\u097F]/g, "")
    .split(/\s+/)
    .filter(w => w && !stopWords.has(w))
    .map(w => w.replace(/s$/, ""));
}

function getStringSimilarity(str1, str2) {
  const tokens1 = new Set(getTokens(str1));
  const tokens2 = new Set(getTokens(str2));
  if (tokens1.size === 0 && tokens2.size === 0) return 1;
  if (tokens1.size === 0 || tokens2.size === 0) return 0;
  let intersection = 0;
  for (const token of tokens1) {
    if (tokens2.has(token)) intersection++;
  }
  const union = tokens1.size + tokens2.size - intersection;
  return intersection / union;
}

exports.getAllComplaints = async (req, res) => {
  try {
    const result = await pool.query("SELECT * FROM complaints ORDER BY created_at DESC");
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "server error" });
  }
};

exports.updateComplaint = async (req, res) => {
  const { id } = req.params;
  const { status } = req.body;
  try {
    await pool.query(
      "UPDATE complaints SET status=$1, updated_at=NOW() WHERE id=$2",
      [status, id]
    );
    res.json({ message: "updated" });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "server error" });
  }
};

exports.createComplaint = async (req, res) => {
  const complaint = req.body.complaint || req.body.complaint_text;

  if (!complaint) {
    return res.status(400).json({ error: "Complaint is required" });
  }

  try {
    const activeComplaintsResult = await pool.query(
      "SELECT id, complaint_text, status FROM complaints WHERE status != 'resolved'"
    );
    for (const existing of activeComplaintsResult.rows) {
      const similarity = getStringSimilarity(complaint, existing.complaint_text);
      if (similarity >= 0.75) {
        return res.status(409).json({
          error: "Duplicate complaint detected. A similar complaint is already registered.",
          duplicate_id: existing.id,
          duplicate_text: existing.complaint_text
        });
      }
    }

    const mlResponse = await axios.post("http://localhost:5000/predict", {
      complaint: complaint,
    });

    let category = (mlResponse.data.category || "").toLowerCase();

    if (category.includes("electric") || category.includes("light") || category.includes("streetlight")) {
      category = "streetlight";
    } else if (category.includes("road") || category.includes("traffic")) {
      category = "road";
    } else if (category.includes("garbage") || category.includes("waste")) {
      category = "garbage";
    } else if (category.includes("water")) {
      category = "water";
    } else if (category.includes("sewage") || category.includes("drain")) {
      category = "sewage";
    } else if (category.includes("encroach")) {
      category = "encroachment";
    }

    const department = departmentMap[category] || "General";
    const priority = getPriority(complaint);

    const now = new Date();
    let deadline = new Date();
    deadline.setDate(now.getDate() + (priority === "high" ? 2 : 4));

    const imagePath = req.file ? `uploads/${req.file.filename}` : null;

    const result = await pool.query(
      `INSERT INTO complaints
       (complaint_text, category, priority, status, department, deadline, created_at, image_path)
       VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
       RETURNING *`,
      [complaint, category, priority, "pending", department, deadline, now, imagePath]
    );

    res.status(201).json({
      message: "Complaint registered",
      data: result.rows[0],
    });

  } catch (error) {
    console.error("ERROR:", error.message);
    res.status(500).json({ error: "Something went wrong" });
  }
};

exports.getComplaintById = async (req, res) => {
  const { id } = req.params;
  try {
    const result = await pool.query("SELECT * FROM complaints WHERE id=$1", [id]);
    if (result.rows.length === 0) {
      return res.status(404).json({ error: "Complaint not found" });
    }
    res.json(result.rows[0]);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Server error" });
  }
};

const { getSLASummary, getSLAAlerts } = require("../services/slaService");

exports.getSLASummary = async (req, res) => {
  try {
    const data = await getSLASummary();
    res.json(data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Server error" });
  }
};

exports.getSLAAlerts = async (req, res) => {
  try {
    const data = await getSLAAlerts();
    res.json(data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Server error" });
  }
};