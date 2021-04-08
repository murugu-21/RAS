import React, { Component } from "react";
import "../App.css";
import axios from "axios";
import { Route, Redirect } from "react-router-dom";
import Alert from "./Alert";
class Login extends Component {
  state = {
    email: "",
    password: "",
    type: "password",
    toggle: "far fa-eye",
    show: false,
    value: "",
  };

  handleChange1 = (event) => {
    this.setState({ email: event.target.value });
  };

  handleChange2 = (event) => {
    this.setState({ password: event.target.value });
  };

  handleSubmit = (event) => {
    axios
      .post("http://localhost:8000/api/loginCheck", {
        email: this.state.email,
        password: this.state.password,
      })
      .then((res) => {
        if (res.data.type) {
          sessionStorage.setItem("email", res.data.email);
          sessionStorage.setItem("type", res.data.type);
          window.location.reload();
        } else {
          this.setState({ show: false });
          this.setState({ show: true, value: res.data });
        }
      });
    event.preventDefault();
  };

  handleVisibility = () => {
    if (this.state.type === "password") {
      this.setState({ type: "text", toggle: "far fa-eye fa-eye-slash" });
    } else {
      this.setState({ type: "password", toggle: "far fa-eye" });
    }
  };

  render() {
    if (sessionStorage.getItem("email") !== null) {
      return (
        <Route>
          <Redirect to="/Home" />
        </Route>
      );
    }
    return (
      <div id="login">
        <div className="bg-img"></div>

        <form onSubmit={this.handleSubmit} className="login">
          <img
            src="https://www.fit2work.com.au/assets/img/avatars/LoginIconAppl.png"
            alt="profilepic"
            className="avatar"
          />
          <h1>Login</h1>
          <p>Email :</p>
          <input
            type="email"
            placeholder="Enter Email"
            onChange={this.handleChange1}
            value={this.state.email}
            required
          />
          <i className="far fa-user-circle"></i>
          <p>Password :</p>
          <input
            type={this.state.type}
            placeholder="Enter Password"
            onChange={this.handleChange2}
            value={this.state.password}
            required
          />
          <i
            className={this.state.toggle}
            id="togglePassword"
            onClick={this.handleVisibility}
          ></i>
          <Alert
            time="3000"
            show={this.state.show}
            type="warning"
            message={this.state.value}
          />
          <input type="submit" name="login_submit" value="submit" />
          <a href="/ForgotPassword">Forgot password</a>
        </form>
      </div>
    );
  }
}

export default Login;
