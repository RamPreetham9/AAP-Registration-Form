import React from "react";
import { useNavigate } from "react-router-dom";
import { getUser, isAuthenticated } from "../services/auth";
import Header from "./Header";

const Home = () => {
  const navigate = useNavigate();
  const user = getUser();

  React.useEffect(() => {
    
    if (!isAuthenticated()) {
      navigate("/login");
    }
  }, [user, navigate]);


  return (
    <div className="home-container">
      <Header /> {/* Render the Header component */}
      <div className="content">
        <h1>Welcome, { user.full_name}</h1>
        <div className="actions">
        </div>
      </div>
    </div>
  );
};

export default Home;
