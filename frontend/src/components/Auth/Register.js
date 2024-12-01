import React, { useState, useEffect } from "react";
import axios from "../../services/api";
import { useNavigate } from "react-router-dom";
import { getUser } from "../../services/auth";

const Register = () => {
  const navigate = useNavigate();

  const user = getUser();
  if (user) {
    navigate("/");
  }
  const [formData, setFormData] = useState({
    full_name: "",
    date_of_birth: "",
    profile_picture: "",
    voter_district: "",
    voter_parliament: "",
    voter_assembly: "",
    voter_mandal: "",
    voter_city: "",
    voter_ward: "",
    mobile_number: "",
    country_code: "+91",
    password: "",
  });

  const [districts, setDistricts] = useState([]);
  const [parliaments, setParliaments] = useState([]);
  const [assemblies, setAssemblies] = useState([]);
  const [mandals, setMandals] = useState([]);
  const [cities, setCities] = useState([]);

  // Fetch dropdown options from the backend
  useEffect(() => {
    const fetchData = async () => {
      try {
        const districtRes = await axios.get("/lists/districts");
        setDistricts(districtRes.data);

        const parliamentRes = await axios.get("/lists/parliaments");
        setParliaments(parliamentRes.data);
      } catch (error) {
        console.error("Failed to fetch data:", error);
      }
    };

    fetchData();
  }, []);

  // Fetch assemblies based on selected parliament
  useEffect(() => {
    if (formData.voter_parliament) {
      const fetchAssemblies = async () => {
        try {
          const res = await axios.get(`/lists/assemblies/`);
          setAssemblies(res.data);
        } catch (error) {
          console.error("Failed to fetch assemblies:", error);
        }
      };

      fetchAssemblies();
    }
  }, [formData.voter_parliament]);

  // Fetch mandals based on selected assembly
  useEffect(() => {
    if (formData.voter_assembly) {
      const fetchMandals = async () => {
        try {
          const res = await axios.get(`/lists/mandals/`);
          setMandals(res.data);
        } catch (error) {
          console.error("Failed to fetch mandals:", error);
        }
      };

      fetchMandals();
    }
  }, [formData.voter_assembly]);

  // Fetch cities based on selected district
  useEffect(() => {
    if (formData.voter_district) {
      const fetchCities = async () => {
        try {
          const res = await axios.get(`/lists/cities/`);
          setCities(res.data);
        } catch (error) {
          console.error("Failed to fetch cities:", error);
        }
      };

      fetchCities();
    }
  }, [formData.voter_district]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log(formData);
  
      // Make a POST request to register the user
      await axios.post("/auth/register", formData);
  
      // Alert the user and redirect to the Verify OTP page
      alert("Registration successful! Check your phone for the OTP.");
      navigate("/verify-otp", { state: { mobile_number: formData.mobile_number } });
    } catch (error) {
      setError(error.response?.data?.error || "Registration failed. Please try again.");
    }
  };
  

  return (
    <div className="container">
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="full_name"
          placeholder="Full Name"
          onChange={handleChange}
          required
        />
        <input
          type="date"
          name="date_of_birth"
          placeholder="Date of Birth"
          onChange={handleChange}
        />
        <input
          type="file"
          name="profile_picture"
          accept="image/*"
          onChange={(e) =>
            setFormData({ ...formData, profile_picture: e.target.files[0] })
          }
        />
        <select
          name="voter_district"
          onChange={handleChange}
          required
          value={formData.voter_district}
        >
          <option value="">Select Voter District</option>
          {districts.map((district) => (
            <option key={district.id} value={district.name}>
              {district.name}
            </option>
          ))}
        </select>
        <select
          name="voter_parliament"
          onChange={handleChange}
          value={formData.voter_parliament}
        >
          <option value="">Select Voter Parliament</option>
          {parliaments.map((parliament) => (
            <option key={parliament.id} value={parliament.id}>
              {parliament.name}
            </option>
          ))}
        </select>
        <select
          name="voter_assembly"
          onChange={handleChange}
          value={formData.voter_assembly}
        >
          <option value="">Select Voter Assembly</option>
          {assemblies.map((assembly) => (
            <option key={assembly.id} value={assembly.id}>
              {assembly.name}
            </option>
          ))}
        </select>
        <select
          name="voter_mandal"
          onChange={handleChange}
          value={formData.voter_mandal}
        >
          <option value="">Select Voter Mandal</option>
          {mandals.map((mandal) => (
            <option key={mandal.id} value={mandal.id}>
              {mandal.name}
            </option>
          ))}
        </select>
        <select
          name="voter_city"
          onChange={handleChange}
          value={formData.voter_city}
        >
          <option value="">Select Voter City</option>
          {cities.map((city) => (
            <option key={city.id} value={city.id}>
              {city.name}
            </option>
          ))}
        </select>
        <input
          type="number"
          name="voter_ward"
          placeholder="Voter Ward No"
          onChange={handleChange}
        />
        <input
          type="text"
          name="mobile_number"
          placeholder="Mobile Number"
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="country_code"
          placeholder="Country Code"
          value={formData.country_code}
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
        <button type="submit">Register</button>
        <p>
          <span>Already registered? </span>
          <button
            type="button"
            className="link-button"
            onClick={() => navigate("/login")}
          >
            Login here
          </button>
        </p>
      </form>
    </div>
  );
};

export default Register;
