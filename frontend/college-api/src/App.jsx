import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainPage from "./components/MainPage";
// import ProfilePage from "./components/ProfilePage";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="*" element={<MainPage />} />
                {/* <Route path='profile' element={<ProfilePage />}/> */}
            </Routes>
        </BrowserRouter>
    );
}

export default App;
