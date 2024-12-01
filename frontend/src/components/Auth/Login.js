import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../../services/api";
import { loginUser } from "../../services/auth";

const Login = () => {
    const [formData, setFormData] = useState({ mobile_number: "", password: "" });
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("/auth/login", formData);
            loginUser(response.data); // Save user data in localStorage
            navigate("/profile"); // Redirect to the profile page after login
        } catch (err) {
            setError(err.response?.data?.error || "Login failed");
        }
    };

    return (
        <div className="container">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Mobile Number"
                    value={formData.mobile_number}
                    onChange={(e) => setFormData({ ...formData, mobile_number: e.target.value })}
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                    required
                />
                {error && <p className="error">{error}</p>}
                <button type="submit">Login</button>
            </form>
            <p className="redirect-text">
                Don’t have an account?{" "}
                <button className="redirect-button" onClick={() => navigate("/register")}>
                    Register here
                </button>
            </p>
        </div>
    );
};

export default Login;
