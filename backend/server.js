const express = require("express");
const app = express();
const cron = require("node-cron");
const path = require("path");
const { checkSLA } = require("./services/slaService");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use("/uploads", express.static(path.join(__dirname, "uploads")));

const complaintRoutes = require("./routes/complaintRoutes");
app.use("/", complaintRoutes);

app.listen(3000, () => {
  console.log("Server running on port 3000");

  cron.schedule("*/1 * * * *", () => {
    console.log("⏱️ Running SLA check...");
    checkSLA();
  });
});