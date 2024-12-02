import React from "react";
import { useNavigate } from "react-router-dom";
import { getUser, clearUser } from "../services/auth";

const Home = () => {
  const navigate = useNavigate();
  const user = getUser();

  React.useEffect(() => {
    if (!user) {
      navigate("/login");
    }
  }, [user, navigate]);

  const handleLogout = () => {
    clearUser(); // Clear user session
    navigate("/login");
  };

  return (
    <div>
      {/* Header */}
      <header style={styles.header}>
        <h2 style={styles.headerText}>Welcome, {user?.full_name || "Guest"}</h2>
        <button onClick={handleLogout} style={styles.logoutButton}>
          Logout
        </button>
      </header>

      {/* Main Content */}
      <div style={styles.container}>
        <h3 style={styles.sectionTitle}>Section 1 Form</h3>
        <form style={styles.form}>
          <input type="text" placeholder="Input 1" style={styles.input} />
          <input type="text" placeholder="Input 2" style={styles.input} />
          <button type="submit" style={styles.submitButton}>
            Submit
          </button>
        </form>

        <h3 style={styles.sectionTitle}>Section 2 Form</h3>
        <form style={styles.form}>
          <input type="text" placeholder="Input A" style={styles.input} />
          <input type="text" placeholder="Input B" style={styles.input} />
          <button type="submit" style={styles.submitButton}>
            Submit
          </button>
        </form>
      </div>
    </div>
  );
};

// Inline Styles
const styles = {
  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "10px 20px",
    backgroundColor: "#007BFF",
    color: "white",
  },
  headerText: {
    margin: 0,
  },
  logoutButton: {
    backgroundColor: "white",
    color: "#007BFF",
    border: "none",
    padding: "5px 10px",
    borderRadius: "5px",
    cursor: "pointer",
    fontWeight: "bold",
    transition: "background-color 0.3s",
  },
  container: {
    padding: "20px",
  },
  sectionTitle: {
    margin: "20px 0 10px",
  },
  form: {
    marginBottom: "20px",
  },
  input: {
    display: "block",
    marginBottom: "10px",
    padding: "8px",
    width: "100%",
    maxWidth: "300px",
    border: "1px solid #ccc",
    borderRadius: "5px",
  },
  submitButton: {
    backgroundColor: "#007BFF",
    color: "white",
    border: "none",
    padding: "10px 20px",
    borderRadius: "5px",
    cursor: "pointer",
    transition: "background-color 0.3s",
  },
};

export default Home;
