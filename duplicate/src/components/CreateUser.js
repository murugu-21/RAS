import React, { Component } from "react";
import axios from "axios";

class CreateUser extends Component {
  state = { email: "", password: "", type: "clerk" };
  handleEmail = (e) => {
    this.setState({ email: e.target.value });
  };
  handlePassword = (e) => {
    this.setState({ password: e.target.value });
  };
  handleType = (e) => {
    this.setState({ type: e.target.value });
  };
  handleSubmit = (e) => {
    axios.post("/api/createUser", this.state).then((res) => {
      if (res.data) {
        alert(this.state.email + " " + res.data);
      }
    });
    e.preventDefault();
  };
  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>email: </label>
        <input
          type="email"
          value={this.state.email}
          onChange={this.handleEmail}
          required
        />
        <br></br>
        <label>password: </label>
        <input
          type="password"
          value={this.state.password}
          onChange={this.handlePassword}
          required
        />
        <br></br>
        <label>
          type:
          <select value={this.state.type} onChange={() => this.handleType}>
            <option value="manager" />
            <option value="clerk" />
            <option value="owner" />
          </select>
        </label>
        <br></br>
        <input type="submit" value="create User" />
      </form>
    );
  }
}

export default CreateUser;
