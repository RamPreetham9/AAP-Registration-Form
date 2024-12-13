import React, { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import axios from "../../services/api";
import { setUser } from "../../services/auth"; // Import setUser for storing authenticated user

const VerifyOtp = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const [otp, setOtp] = useState("");
  const [error, setError] = useState("");

  // Get mobile number from location state
  const { mobile_number } = location.state || {};

  const handleOtpChange = (e) => {
    setOtp(e.target.value);
  };

  const handleOtpSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("/auth/verify-otp", {
        mobile_number,
        otp,
      });

      if (response.data.success) {
        alert(response.data.message);

        const userData = response.data.user; // Extract user data from response
        console.log(response.data);
        
        if (userData) {
          setUser(userData);
        }

        // Redirect based on registration or reset password case
        if (response.data.is_registration) {
          navigate("/complete-registration"); // Home page for new registrations
        }
      } else {
        setError("Verification failed. Please try again.");
      }
    } catch (error) {
      console.error(error);
      setError(
        error.response?.data?.error || "Failed to verify OTP. Please try again."
      );
    }
  };

  return (
    <div className="container">
      <h2>Verify OTP</h2>
      {error && <p className="error">{error}</p>}
      <p>Enter the OTP sent to {mobile_number}</p>
      <form onSubmit={handleOtpSubmit}>
        <input
          type="text"
          name="otp"
          placeholder="Enter OTP"
          value={otp}
          onChange={handleOtpChange}
          required
        />
        <button type="submit">Verify OTP</button>
      </form>
      <button
        type="button"
        className="link-button"
        onClick={() => navigate("/reset-password")}
      >
        Edit Mobile Number
      </button>
    </div>
  );
};

export default VerifyOtp;
