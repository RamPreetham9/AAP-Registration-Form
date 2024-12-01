import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../../services/api";

const ResetPassword = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    mobile_number: "",
    country_code: "+91",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("/auth/request-reset-password", formData);
      alert("OTP sent to your phone. Please check your messages.");
      navigate("/login");
    } catch (error) {
      console.error(error);
      alert("Failed to send OTP. Please try again.");
    }
  };

  return (
    <div className="container">
      <h2>Forgot Password</h2>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <input
            type="text"
            name="country_code"
            className="country-code"
            value={formData.country_code}
            onChange={handleChange}
            required
          />
          <input
            type="text"
            name="mobile_number"
            placeholder="Mobile Number"
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Request OTP</button>
        <button
          type="button"
          className="link-button"
          onClick={() => navigate("/login")}
        >
          Back to Login
        </button>
      </form>
    </div>
  );
};

export default ResetPassword;
