import React, {Component} from 'react';
import { Navbar, Nav, NavDropdown, Dropdown } from 'react-bootstrap'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUserCircle } from '@fortawesome/free-regular-svg-icons'
import {Link} from 'react-router-dom';
import { connect } from 'react-redux';


import {auth} from '../../../config/firebase';
import { changeAuthState } from '../../../actions';

import '../../../assets/css/Navigation.css';
import DefaultUserImage from '../../../assets/images/profile_placeholder.png';
import logo from '../../../assets/images/LOGO.png' 
class Navigation extends Component{

    onSignOut = () => {
        auth.signOut()
        .then((response) => {
            this.props.changeAuthState(null);
        })
        .catch(err => {
            console.error(err);
        })
    }

    renderUserImage = (imageUrl) => {
        return (
            <img src={imageUrl} className="user-image" />
        )
    }

    render = () => {
        return (
            <Navbar collapseOnSelect expand="lg" bg="light" variant="light" id="navigation" style={{padding:"0"}}>
                <div className="container">
                    <Navbar.Brand href="https://d360.studio/" target="__blank"><img src={logo} alt="V360" style={{height:"50px", paddingBottom:"10px"}}/></Navbar.Brand>
                    {/* <Navbar.Brand style={{fontSize:'20px', fontWeight:'80px'}}>DInsight Messenger</Navbar.Brand> */}
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse  id="responsive-navbar-nav">
                        <Nav className="mr-auto">
                            <Nav.Link>
                                <Link to='/' style={{fontSize:"15px"}}>DInsight Messenger</Link>
                            </Nav.Link>
                            {/* <Nav.Link >
                                <Link to='/inventory'>Inventory</Link>
                            </Nav.Link> */}
                            <Nav.Link>
                                <Link to='/analysis' style={{fontSize:"15px"}}>Analysis</Link>
                            </Nav.Link>
                        </Nav>
                        <Nav className ="ms-auto align-middle">
                            <NavDropdown  title={
                                <>
                                    <span> {this.renderUserImage(this.props.imageUrl || DefaultUserImage)} {this.props.displayName}</span>
                                </>
                            } id="basic-nav-dropdown">
                                <NavDropdown.Item >Profile</NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item onClick={this.onSignOut}>Log out</NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>
                </div>
            </Navbar>
        )
    }
}

const mapStateToProps = (state) => {
    if (!state.user)return {}
    return {
        imageUrl : state.user.photoURL,
        displayName : state.user.displayName
    };
}

export default connect(mapStateToProps, {changeAuthState})(Navigation);