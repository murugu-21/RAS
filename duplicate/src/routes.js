import Login from "./components/Login.js";
import Home from "./components/Home.js";
import CreateUser from "./components/CreateUser.js";
import ForgotPassword from "./components/ForgotPassword.js";
import Otp from "./components/Otp.js";
import ChangePassword from "./components/ChangePassword.js";
import LogOut from "./components/LogOut.js";
import Profile from "./components/Profile.js";
import About from "./components/About.js";
import Support from "./components/Support.js";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

const Routes = () => (
  <Router>
    <Switch>
      <Route exact path="/" component={Login} />
      <Route path="/Home" component={Home} />
      <Route path="/CreateUser" component={CreateUser} />
      <Route path="/ForgotPassword" component={ForgotPassword} />
      <Route path="/Otp" component={Otp} />
      <Route path="/ChangePassword" component={ChangePassword} />
      <Route path="/Profile" component={Profile} />
      <Route path="/About" component={About} />
      <Route path="/Support" component={Support} />
      <Route path="/LogOut" component={LogOut} />
    </Switch>
  </Router>
);

export default Routes;
