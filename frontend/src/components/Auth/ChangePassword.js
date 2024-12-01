import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../../services/api";

const ChangePassword = () => {
  const navigate = useNavigate();
  const [password, setPassword] = useState("");

  useEffect(() => {
    // Redirect to /reset-password if the user hasn't verified OTP
    const isOtpVerified = sessionStorage.getItem("otpVerified") === "true";
    if (!isOtpVerified) {
      navigate("/reset-password");
    }
  }, [navigate]);

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handlePasswordSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.patch("/auth/change-password", { password });
      alert(response.data.message);
      if (response.data.success) {
        navigate("/login");
      }
    } catch (error) {
      console.error(error);
      alert("Failed to update password. Please try again.");
    }
  };

  return (
    <div className="container">
      <h2>Change Password</h2>
      <form onSubmit={handlePasswordSubmit}>
        <input
          type="password"
          name="password"
          placeholder="New Password"
          value={password}
          onChange={handlePasswordChange}
          required
        />
        <button type="submit">Update Password</button>
      </form>
    </div>
  );
};

export default ChangePassword;
