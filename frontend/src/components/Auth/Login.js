import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../../services/api";
import { setUser, isAuthenticated } from "../../services/auth";

const Login = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    mobile_number: "",
    password: "",
  });

  React.useEffect(() => {
    if (isAuthenticated()) {
      navigate("/");
    }
  }, [navigate]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("/auth/login", formData);
      setUser(response.data);
      navigate("/");
    } catch (error) {
      if (error.response && error.response.status === 404) {
        alert("User not found. Redirecting to registration page.");
        navigate("/register");
      } else {
        console.error(error);
        alert("Login failed. Please check your credentials.");
      }
    }
  };

  return (
    <div className="container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="mobile_number"
          placeholder="Mobile Number"
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
          required
        />
        <button type="submit">Login</button>
      </form>
      <p>
        <button onClick={() => navigate("/reset-password")} className="link-button">
          Forgot Password?
        </button>
      </p>
      <p>
        <span>New user? </span>
        <button onClick={() => navigate("/register")} className="link-button">
          Register here
        </button>
      </p>
    </div>
  );
};

export default Login;
