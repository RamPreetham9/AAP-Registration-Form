import React from "react";
import { useNavigate } from "react-router-dom";
import { clearUser, getUser } from "../services/auth";

const Header = () => {
    const navigate = useNavigate();
    const user = getUser();
    console.log(user.user);
    

    const handleLogout = () => {
        clearUser();
        navigate("/login");
    };

    return (
        <header className="header">
            <div className="header-left">
                <h1>{user?.user.full_name || "Guest"}</h1>
            </div>
            <div className="header-right">
                <button
                    className="header-button"
                    onClick={() => navigate("/")}
                >
                    Home
                </button>
                <button
                    className="header-button"
                    onClick={() => navigate("/volunteering")}
                >
                    Volunteer Form
                </button>
                <button
                    className="header-button"
                    onClick={() => navigate("/election-form")}
                >
                    Election Form
                </button>

                <button className="logout-button" onClick={handleLogout}>
                    Logout
                </button>
            </div>
        </header>
    );
};

export default Header;
