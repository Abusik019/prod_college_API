import "./App.css";
import { Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import Login from './pages/Login';
import Structure from './pages/Structure';
import Documents from './pages/Docs';
import Applicants from "./pages/Applicants";
import Profile from "./pages/Profile";


function App() {
    return (
        <Routes>
            <Route path="*" element={<Main />} />
            <Route path='/login' element={<Login />}/>
            <Route path='/structure' element={<Structure />}/>
            <Route path='/documents' element={<Documents />}/>
            <Route path='/applicants' element={<Applicants />}/>
            <Route path='/profile' element={<Profile />}/>
        </Routes>
    );
}

export default App;
