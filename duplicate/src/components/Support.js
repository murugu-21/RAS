import Navbar from "./Navbar";
import { Redirect } from "react-router-dom";
const Support = () => {
  if (sessionStorage.getItem("type") === null) {
    return <Redirect to="/" />;
  }
  return (
    <div>
      <Navbar />
      <div>
        <h3>For any queries mail to manager@gmail.com</h3>
      </div>
    </div>
  );
};

export default Support;
