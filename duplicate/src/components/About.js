import { Redirect } from "react-router";
import Navbar from "./Navbar";

const About = () => {
  if (sessionStorage.getItem("type") === null) {
    return <Redirect to="/" />;
  }
  return (
    <div>
      <Navbar />
      <div>
        <h3>
          This is a website to automate restaurant operations and inventory
          management
        </h3>
        <h4>Purely meant for educational purposes</h4>
      </div>
    </div>
  );
};

export default About;
