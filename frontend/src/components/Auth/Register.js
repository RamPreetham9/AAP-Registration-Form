import React, { useState, useEffect } from "react";
import axios from "../../services/api";

const Register = () => {
    const [formData, setFormData] = useState({
        full_name: "",
        date_of_birth: "",
        profile_picture: null,
        voter_district: "",
        voter_parliament: "",
        voter_assembly: "",
        voter_mandal: "",
        voter_city: "",
        voter_ward_no: "",
    });

    const [districts, setDistricts] = useState([]); // Holds the districts for the dropdown
    const [errors, setErrors] = useState({}); // To handle validation errors

    // Fetch districts from the correct endpoint
    useEffect(() => {
        const fetchDistricts = async () => {
            try {
                const response = await axios.get("/api/districts"); // Correct endpoint
                setDistricts(response.data);
            } catch (err) {
                console.error("Error fetching districts:", err);
            }
        };
        fetchDistricts();
    }, []);
    

    const validateForm = () => {
        const newErrors = {};
        if (!formData.full_name) newErrors.full_name = "Full Name is required.";
        if (!formData.voter_district) newErrors.voter_district = "Voter District is required.";
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!validateForm()) return;

        // Prepare form data for submission
        const formDataToSend = new FormData();
        Object.keys(formData).forEach((key) => {
            formDataToSend.append(key, formData[key]);
        });

        try {
            const response = await axios.post("/api/auth/register", formDataToSend);
            alert("Registration successful!");
        } catch (err) {
            console.error("Registration failed:", err);
        }
    };

    return (
        <div className="container">
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <label>Full Name *</label>
                <input
                    type="text"
                    value={formData.full_name}
                    onChange={(e) => setFormData({ ...formData, full_name: e.target.value })}
                />
                {errors.full_name && <p className="error">{errors.full_name}</p>}

                <label>Date of Birth (Optional)</label>
                <input
                    type="date"
                    value={formData.date_of_birth}
                    onChange={(e) => setFormData({ ...formData, date_of_birth: e.target.value })}
                />

                <label>Profile Picture (Optional)</label>
                <input
                    type="file"
                    onChange={(e) => setFormData({ ...formData, profile_picture: e.target.files[0] })}
                />

                <label>Voter District *</label>
                <select
                    value={formData.voter_district}
                    onChange={(e) => setFormData({ ...formData, voter_district: e.target.value })}
                >
                    <option value="">Select District</option>
                    {districts.map((district) => (
                        <option key={district.id} value={district.id}>
                            {district.name}
                        </option>
                    ))}
                </select>
                {errors.voter_district && <p className="error">{errors.voter_district}</p>}

                <label>Voter Parliament (Optional)</label>
                <input
                    type="text"
                    value={formData.voter_parliament}
                    onChange={(e) => setFormData({ ...formData, voter_parliament: e.target.value })}
                />

                <label>Voter Assembly (Optional)</label>
                <input
                    type="text"
                    value={formData.voter_assembly}
                    onChange={(e) => setFormData({ ...formData, voter_assembly: e.target.value })}
                />

                <label>Voter Mandal (Optional)</label>
                <input
                    type="text"
                    value={formData.voter_mandal}
                    onChange={(e) => setFormData({ ...formData, voter_mandal: e.target.value })}
                />

                <label>Voter City (Optional)</label>
                <input
                    type="text"
                    value={formData.voter_city}
                    onChange={(e) => setFormData({ ...formData, voter_city: e.target.value })}
                />

                <label>Voter Ward No (Optional)</label>
                <input
                    type="text"
                    value={formData.voter_ward_no}
                    onChange={(e) =>
                        setFormData({ ...formData, voter_ward_no: e.target.value.replace(/\D/g, "") })
                    }
                />

                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default Register;
