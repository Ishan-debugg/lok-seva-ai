const pool = require("./config/db");

async function migrate() {
  try {
    console.log("Starting database migration...");
    await pool.query(`
      ALTER TABLE complaints 
      ADD COLUMN IF NOT EXISTS image_path VARCHAR(255);
    `);
    console.log("✅ Column 'image_path' added successfully or already exists.");
    process.exit(0);
  } catch (error) {
    console.error("❌ Migration failed:", error);
    process.exit(1);
  }
}

migrate();
