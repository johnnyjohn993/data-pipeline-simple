const db = require('../config/database');

exports.signup = async (req, res) => {
  const { username, email, password } = req.body;
  try {
    const [result] = await db.execute(
      'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
      [username, email, password] // Note: In production, hash this password!
    );
    res.status(201).json({ message: 'User registered successfully', userId: result.insertId });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};
