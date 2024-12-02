import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Register from "./components/Auth/Register";
import VerifyOtp from "./components/Auth/VerifyOtp";
import Login from "./components/Auth/Login";
import Home from "./components/Home";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/verify-otp" element={<VerifyOtp />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;
