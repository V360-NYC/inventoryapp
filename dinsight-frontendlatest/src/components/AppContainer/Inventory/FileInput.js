import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMinusCircle } from '@fortawesome/free-solid-svg-icons';

class FileInput extends React.Component{
  
    onFileSelect = (event)=>{
  
        this.props.onFileSelect(event.target.id, event.target.files[0]);
    }

    render(){
        return  (
            <div className="input-group">
                <input 
                    id={this.props.id} 
                    key={this.props.id}
                    className="form-control" 
                    type="file" 
                    onChange={this.onFileSelect}
                    required
                />
                <span className="input-group-text bg-danger">
                    <a onClick={() => this.props.removeFileInput(this.props.id)}>
                        <FontAwesomeIcon icon={faMinusCircle} className="text-white" />
                    </a>
                </span>
            </div>
        )
    }
}

export default FileInput;