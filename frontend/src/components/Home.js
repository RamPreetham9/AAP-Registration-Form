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
      <h1>Welcome, {user?.full_name || "Guest"}</h1>
      <p>This is the home page. You’re successfully logged in.</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Home;
