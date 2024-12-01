import React, { useState, useEffect } from "react";
import axios from "../../services/api";

const Profile = () => {
    const [profile, setProfile] = useState({});
    const [updatedProfile, setUpdatedProfile] = useState({});
    const [message, setMessage] = useState("");

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await axios.get("/profile/1");
                setProfile(response.data);
            } catch (err) {
                console.error(err);
            }
        };
        fetchProfile();
    }, []);

    const handleUpdate = async () => {
        try {
            const response = await axios.put(`/profile/update/1`, updatedProfile);
            setMessage(response.data.message);
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <div className="container profile-card">
            <h2>Profile</h2>
            <input
                type="text"
                value={updatedProfile.full_name || profile.full_name || ""}
                onChange={(e) => setUpdatedProfile({ ...updatedProfile, full_name: e.target.value })}
                placeholder="Full Name"
            />
            <button onClick={handleUpdate}>Update Profile</button>
            {message && <p className="success">{message}</p>}
        </div>
    );
};

export default Profile;
