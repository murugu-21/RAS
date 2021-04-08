import React, { Component } from "react";
import axios from "axios";
import { Redirect } from "react-router-dom";
import Expire from "./Expire.js";
class ChangePassword extends Component {
  state = {
    password: "",
    cnf_password: "",
    value: "",
  };

  handleChange = (event) => {
    this.setState({ password: event.target.value });
  };

  handleChange1 = (event) => {
    this.setState({ cnf_password: event.target.value });
  };

  handleSubmit = (event) => {
    if (this.state.password !== this.state.cnf_password) {
      alert("Password don't match");
    } else {
      axios
        .post("/api/ChangePassword", {
          email: sessionStorage.getItem("requestEmail"),
          password: this.state.password,
          otp: sessionStorage.getItem("otp"),
        })
        .then((res) => {
          console.log(res.data.cango);
          if (res.data.cango) {
            alert("password changed...!");
            sessionStorage.removeItem("requestEmail");
            sessionStorage.removeItem("otp");
            this.props.history.push("/");
          } else {
            this.setState({ value: res.data });
          }
        });
      event.preventDefault();
    }
  };

  render() {
    if (sessionStorage.getItem("otp") !== null) {
      return (
        <div>
          <h1>Change Password</h1>
          <form onSubmit={this.handleSubmit} className="login">
            <p>Enter Password</p>
            <input
              type="password"
              onChange={this.handleChange}
              value={this.state.password}
              placeholder="Enter Password"
              required
            />
            <p>Confirm password</p>
            <input
              type="password"
              onChange={this.handleChange1}
              value={this.state.cnf_password}
              placeholder="Re-enter password"
              required
            />
            <input type="submit" name="login_submit" value="submit" />
            <a href="/">Login</a>
          </form>
          <Expire delay="3000">
            {
              <div class="alert alert-warning" role="alert">
                {this.state.value}
              </div>
            }
          </Expire>
        </div>
      );
    } else {
      return <Redirect to="/" />;
    }
  }
}

export default ChangePassword;
