import React, { Component } from "react";
import axios from "axios";

class ForgotPassword extends Component {
  state = {
    email: "",
  };

  handleChange = (event) => {
    this.setState({ email: event.target.value });
  };

  handleSubmit = (event) => {
    sessionStorage.setItem("requestEmail", this.state.email);
    axios
      .post("/api/ForgotPassword", {
        email: this.state.email,
      })
      .then((res) => {
        console.log(res.data.cango);
        if (res.data.cango) {
          this.props.history.push("/Otp");
        } else {
          alert(res.data);
        }
      });
    event.preventDefault();
  };

  render() {
    return (
      <div>
        <h1>Forgot Password</h1>
        <form onSubmit={this.handleSubmit} className="login">
          <p>Enter Email</p>
          <input
            type="email"
            placeholder="Enter Email"
            onChange={this.handleChange}
            value={this.state.email}
            required
          />
          <input type="submit" name="login_submit" value="submit" />
          <a href="/">Login</a>
        </form>
      </div>
    );
  }
}

export default ForgotPassword;
