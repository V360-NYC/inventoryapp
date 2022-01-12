import React from 'react';
import DisplayInventory from '../Inventory/DisplayInventory';
import SendEmailModal from './SendEmailModal';

class Analysis extends React.Component{
    state = {
        show : false
    }
    showModal = () => {
        this.setState({
            show:true
        })
    }
    handleClose = () => {
        this.setState({
            show : false
        })
    }

    render(){
        return (
            <div className="container">
                {/* <SendEmailModal show={this.state.show} handleClose={this.handleClose} />
                <div className="row p-4">
                    <div className="col text-center">
                        <div className="display-6">Summary Reports</div>
                    </div>
                    
                </div>
                <div className="row justify-content-center">
                    <div className="col">
                        <div className="row">
                            <div className="col">
                                <button className="btn btn-primary float-end">Get sharable Link</button>
                            </div>
                            <div className="col">
                            <button className="btn btn-primary" onClick={this.showModal}>Send report via email</button>
                            </div>
                        </div>
                    </div>
                </div> */}
                <div className="row">
                    <div className="col">
                        <DisplayInventory/>
                    </div>
                </div>
            </div>
        )
    }
}

export default Analysis;