const express = require("express");
const router = express.Router();
const multer = require("multer");
const path = require("path");

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "uploads/");
  },
  filename: function (req, file, cb) {
    const uniqueSuffix = Date.now() + "-" + Math.round(Math.random() * 1E9);
    cb(null, uniqueSuffix + path.extname(file.originalname));
  }
});

const upload = multer({ storage: storage });

const {
  createComplaint,
  getComplaintById,
  getAllComplaints,
  updateComplaint,
  getSLASummary,
  getSLAAlerts
} = require("../controllers/complaintController");

router.post("/complaints", upload.single("image"), createComplaint);
router.get("/complaints", getAllComplaints);
router.get("/complaints/:id", getComplaintById);
router.put("/complaints/:id", updateComplaint);

router.get("/sla/summary", getSLASummary);
router.get("/sla/alerts",  getSLAAlerts);

module.exports = router;