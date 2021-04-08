import React, { Component } from "react";
import axios from "axios";
import Tabs from "./Tabs.js";
import Statisticalreport from "./statisticalreport.js";
import FoodPrice from "./FoodPrice.js";
import Addfooditems from "./Addfooditems.js";
import Ingredients from "./Ingredients.js";
class Manager extends Component {
  makeReport = (event) => {
    axios.post("/api/CreatePdf", {}).then((res) => {
      alert("report generated");
    });
    event.preventDefault();
  };

  render() {
    return (
      <Tabs>
        <div label="Sales Report">
          <input
            type="button"
            onClick={this.makeReport}
            value="generate report"
          />
          <Statisticalreport />
        </div>
        <div label="Food List">
          <FoodPrice />
        </div>
        <div label="Add Food">
          {/* <Addfooditems /> */}
          <Ingredients />
        </div>
      </Tabs>
    );
  }
}

export default Manager;
