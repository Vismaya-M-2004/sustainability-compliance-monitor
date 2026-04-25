import { Routes, Route } from "react-router-dom";
import ListPage from "./pages/ListPage";
import FormPage from "./pages/FormPage";
import LoginPage from "./pages/LoginPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<ListPage />} />
      <Route path="/add" element={<FormPage />} />
      <Route path="/login" element={<LoginPage />} />
    </Routes>
  );
}

export default App;