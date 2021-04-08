import Navbar from "./Navbar";
import { Redirect } from "react-router-dom";
const Profile = () => {
  if (sessionStorage.getItem("type") === null) {
    return <Redirect to="/" />;
  }
  return (
    <div>
      <Navbar />
      <div>
        <h3>Email : {sessionStorage.getItem("email")}</h3>
        <h3>Type : {sessionStorage.getItem("type")}</h3>
      </div>
    </div>
  );
};

export default Profile;
