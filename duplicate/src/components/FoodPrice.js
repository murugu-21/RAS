import axios from "axios";
import React, { Component } from "react";
import "./FoodPrice.css";
import Expire from "./Expire.js";
class FoodPrice extends Component {
  state = { FoodList: [], changed: {}, value: "" };
  componentDidMount() {
    axios.post("http://localhost:8000/api/GetFoods").then((response) => {
      this.setState({ FoodList: response.data });
    });
  }
  handleAdd = (item, index) => {
    item[2] = item[2] + 1;
    let temp = [...this.state.FoodList];
    let newChange = {};
    Object.assign(newChange, this.state.changed);
    temp[index][2] = item[2];
    newChange[item[0]] = item[2];
    temp[index][2] = item[2];
    this.setState({ FoodList: temp, changed: newChange });
  };
  handleSub = (item, index) => {
    if (item[2] > 5) {
      item[2] = item[2] - 1;
      let temp = [...this.state.FoodList];
      let newChange = {};
      Object.assign(newChange, this.state.changed);
      temp[index][2] = item[2];
      newChange[item[0]] = item[2];
      temp[index][2] = item[2];
      this.setState({ FoodList: temp, changed: newChange });
    } else {
      alert("Price cannot be less than 5");
    }
  };
  updatDb = () => {
    axios.post("api/UpdatePrice", this.state.changed).then((response) => {
      this.setState({ value: response.data });
    });
  };
  render() {
    return (
      <div>
        <table>
          <thead>
            <tr>
              <th>Item Code</th>
              <th>Name</th>
              <th>Price</th>
            </tr>
          </thead>
          <tbody>
            {this.state.FoodList.map((item, index) => {
              return (
                <tr key={item[0]}>
                  <td>{item[0]}</td>
                  <td>{item[1]}</td>
                  <td>
                    {" "}
                    <button
                      className="buttonSub"
                      onClick={() => this.handleSub(item, index)}
                    >
                      <i className=""></i> -{" "}
                    </button>
                    {item[2]}{" "}
                    <button
                      className="buttonAdd"
                      onClick={() => this.handleAdd(item, index)}
                    >
                      <i className=""></i> +{" "}
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
        <button
          onClick={this.updatDb}
          disabled={Object.entries(this.state.changed).length === 0}
        >
          Update Prices
        </button>
        {this.state.value === "success" && (
          <Expire delay="3000">
            <div className="alert alert-success" role="alert">
              success price list updated
            </div>
          </Expire>
        )}
        {this.state.value === "db error" && (
          <Expire delay="3000">
            <div className="alert alert-danger" role="alert">
              Price list not updated, Try again later
            </div>
          </Expire>
        )}
      </div>
    );
  }
}

export default FoodPrice;
