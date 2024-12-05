import React, { useState, useEffect } from "react";
import axios from "../../services/api";
import Header from "../Header";

const Complaints = () => {
  const [districts, setDistricts] = useState([]);
  const [municipalities, setMunicipalities] = useState([]);
  const [formData, setFormData] = useState({
    district: "",
    municipality: "",
    complaint_text: "",
    file: null,
  });
  const [successMessage, setSuccessMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    const fetchDistricts = async () => {
      try {
        const response = await axios.get("/lists/districts");
        setDistricts(response.data);
      } catch (error) {
        console.error("Error fetching districts:", error);
      }
    };
    fetchDistricts();
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleFileChange = (e) => {
    setFormData({ ...formData, file: e.target.files[0] });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData();
    data.append("user_id", localStorage.getItem("user_id")); // Assuming user_id is in localStorage
    data.append("district", formData.district);
    data.append("municipality", formData.municipality);
    data.append("complaint_text", formData.complaint_text);
    data.append("file", formData.file);

    try {
      const response = await axios.post("/complaints", data);
      setSuccessMessage(response.data.message);
      setErrorMessage("");
      setFormData({
        district: "",
        municipality: "",
        complaint_text: "",
        file: null,
      });
    } catch (error) {
      setErrorMessage(error.response?.data?.error || "Failed to submit complaint");
      setSuccessMessage("");
    }
  };

  return (
    <div className="container">
        <Header />
      <h2>Submit a Complaint</h2>
      {successMessage && <p className="success">{successMessage}</p>}
      {errorMessage && <p className="error">{errorMessage}</p>}
      <form onSubmit={handleSubmit}>
        <select name="district" value={formData.district} onChange={handleChange} required>
          <option value="">Select District</option>
          {districts.map((district) => (
            <option key={district.id} value={district.name}>
              {district.name}
            </option>
          ))}
        </select>

        <input
          type="text"
          name="municipality"
          placeholder="Enter Municipality"
          value={formData.municipality}
          onChange={handleChange}
          required
        />

        <textarea
          name="complaint_text"
          placeholder="Enter your complaint"
          value={formData.complaint_text}
          onChange={handleChange}
          required
        ></textarea>

        <input type="file" name="file" onChange={handleFileChange} accept="image/*" required />

        <button type="submit">Submit Complaint</button>
      </form>
    </div>
  );
};

export default Complaints;
