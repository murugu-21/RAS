import React, { Component } from "react";
//import "./table.css";
import axios from "axios";
import Websocket from "react-websocket";
class Users extends Component {
  state = { result: [] };
  componentDidMount() {
    axios
      .post("/api/getUsers")
      .then((response) => {
        let userArr = response.data;
        if (userArr.length !== 0) {
          this.setState({ result: userArr });
        }
      })
      .catch((error) => console.log(error));
    let eventSource = new EventSource("/event");
    eventSource.onmessage = (e) => {
      console.log("working", e);
      this.setState({ result: JSON.parse(e.data) });
    };
  }
  handleOperation = (item) => {
    console.log(item);
    axios
      .post("/api/deleteUsers", { email: item.email })
      .then((response) => {
        let userArr = response.data;
        if (userArr.length !== 0) {
          this.setState({ result: userArr });
        }
      })
      .catch((error) => console.log(error));
  };
  handleDbChange = (data) => {
    this.setState({ result: JSON.parse(data) });
  };
  render() {
    return (
      <div>
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
                      <i class="fa fa-trash"></i> remove{" "}
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
        <Websocket
          url="ws://localhost:8000/live/product/12345/"
          onMessage={this.handleDbChange}
        />
      </div>
    );
  }
}

export default Users;
