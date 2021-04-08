import React, { Component } from "react";
import "./table.css";
import Tabs from "./Tabs.js";
import axios from "axios";
import Alert from "./Alert";
class Owner extends Component {
  state = {
    result: [],
    email: "",
    password: "",
    type: "clerk",
    InputType: "password",
    toggle: "far fa-eye",
    showalert: false,
    value: "",
    showPass: false,
    passValue: "",
  };

  componentDidMount() {
    axios

      .post("http://localhost:8000/api/getUsers")

      .then((response) => {
        let userArr = response.data;

        if (userArr.length !== 0) {
          this.setState({ result: userArr });
        }
      })

      .catch((error) => console.log(error));
  }

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
    axios
      .post("http://localhost:8000/api/createUser", {
        email: this.state.email,
        password: this.state.password,
        type: this.state.type,
      })
      .then((res) => {
        if (res.data === "success") {
          this.setState({
            email: "",
            password: "",
            type: "clerk",
            InputType: "password",
            toggle: "far fa-eye",
            passValue: res.data,
          });
          axios

            .post("http://localhost:8000/api/getUsers")

            .then((response) => {
              let userArr = response.data;

              if (userArr.length !== 0) {
                this.setState({ result: userArr });
              }
            })

            .catch((error) => console.log(error));
        } else {
          this.setState({ showPass: false });
          this.setState({ showPass: true, passValue: res.data });
        }
      });
    e.preventDefault();
  };

  handleOperation = (item) => {
    if (item.type === "owner") {
      this.setState({ showalert: false });
      this.setState({ showalert: true, value: "Owner cannot be deleted" });
    } else {
      axios

        .post("http://localhost:8000/api/deleteUser", { email: item.email })

        .then((response) => {
          let userArr = response.data;

          if (userArr.length !== 0 && typeof userArr === "object") {
            this.setState({ result: userArr });
          } else {
            this.setState({ showalert: false });
            this.setState({ showalert: true, value: userArr });
          }
        })

        .catch((error) => console.log(error));
    }
  };

  handleVisibility = () => {
    if (this.state.InputType === "password") {
      this.setState({ InputType: "text", toggle: "far fa-eye fa-eye-slash" });
    } else {
      this.setState({ InputType: "password", toggle: "far fa-eye" });
    }
  };

  render() {
    return (
      <Tabs>
        <div label="Users">
          <table>
            <thead>
              <tr>
                <th>Email</th>
                <th>type</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {this.state.result.map((item) => {
                return (
                  <tr key={item.email}>
                    <td>{item.email}</td>
                    <td>{item.type}</td>
                    <td>
                      {" "}
                      <button
                        className="buttondecor"
                        onClick={() => this.handleOperation(item)}
                      >
                        <i className="fa fa-trash"></i> remove{" "}
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          <Alert
            show={this.state.showalert}
            message={this.state.value}
            type="warning"
            time="3000"
          />
        </div>

        <div label="Create User">
          <div className="center">
            <form onSubmit={this.handleSubmit}>
              <label>
                email:{" "}
                <input
                  type="email"
                  value={this.state.email}
                  onChange={this.handleEmail}
                  required
                />
              </label>
              <br></br>
              <label>
                password:{" "}
                <input
                  type={this.state.InputType}
                  value={this.state.password}
                  onChange={this.handlePassword}
                  required
                />
                <i
                  className={this.state.toggle}
                  id="togglePassword"
                  onClick={this.handleVisibility}
                ></i>
                <Alert
                  time="3000"
                  type="warning"
                  show={this.state.showPass}
                  message={this.state.passValue}
                />
              </label>
              <br></br>
              <label>
                type:{" "}
                <select value={this.state.type} onChange={this.handleType}>
                  <option value="manager">Manager</option>
                  <option value="clerk">Clerk</option>
                  <option value="owner">Owner</option>
                </select>
              </label>
              <br></br>
              <input type="submit" value="create User" />
            </form>
          </div>
          <Alert
            time="5000"
            show={this.state.passValue === "success"}
            type="success"
            message={this.state.passValue}
          />
        </div>
      </Tabs>
    );
  }
}

export default Owner;
