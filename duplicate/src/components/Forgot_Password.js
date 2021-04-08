import React, { Component } from 'react';
import axios from "axios";
import {Redirect} from 'react-router-dom';

class Forgot_Password extends Component {
    state = {
        email: "",
    };

    handleChange = (event) => {
        this.setState({ email: event.target.value });
    };
    
      handleSubmit = (event) => {
        sessionStorage.setItem("requestEmail", this.state.email);
        axios
          .post("http://localhost:8000/api/ForgotPassword", {
            email: this.state.email
          })
          .then((res) => {
              console.log(res.data.cango);
            if (res.data.cango) {
                this.props.history.push("/Otp");              
            } else {
              alert(this.state.email + res.data);
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
 
export default Forgot_Password;