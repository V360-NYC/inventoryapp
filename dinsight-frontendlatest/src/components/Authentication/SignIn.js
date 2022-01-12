import React, {Component} from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {auth, authProviders} from '../../config/firebase';

class SignIn extends Component{


    handleGoogleSignIn = (event) => {
        event.preventDefault();
        
        auth.signInWithPopup(authProviders.googleAuthProvider)
        .then((response) => {
            
        })
        .catch(err => {
            console.error(err)
        });   
    }

    render = () => {
        return (
            <div className="container">
            <div className="row">
                <div className="col-lg-4 col-md-3 col-sm-6 col-6"></div>
                <div className="col-lg-4 col-md-6 p-3">
                    {/* <div className="alert alert-danger" >{{ error_message }} </div> */}
                    <div className="card text-center" >
                        <div className="header my-3">Login Form</div>
                        <div className="card-body">
                            <form >
                                <div className="form-group">
                                    <label for="email">email</label>
                                    <input type="email" id="email" className="form-control"  name="email" />
                                </div>
                                <div className="form-group">
                                    <label for="password">password</label>
                                    <input type="password" id="password" className="form-control"  name="password" />
                                </div>
                                <button className="m-3 btn btn-primary" type="submit"> Log In</button>
                                <div className="p-3">
                                    Or
                                </div>
                                <div className="p-3">
                                    <button className="btn btn-danger" onClick={this.handleGoogleSignIn}>
                                        <span><FontAwesomeIcon icon={['fab','google']} /> SignIn with Google</span>
                                    </button>
                                </div>
                                <div className="p-3">
                                    Don't have an Account? <a href="">Sign Up</a>
                                </div>
                                
                            </form>
                        </div>
                    </div>       
                </div>
                <div className="col"></div>
            </div>    
        </div>
        )
    }
}

export default SignIn;