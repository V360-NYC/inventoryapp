
import React from 'react';
import LoadingSpinner from '../util/LoadingSpinner';
import DataTable from './DataTable';
import QuickSearch from './quickSearch';

class MessageDetail extends React.Component{
    renderChild = () => {
        // console.log(this.props)
        if(this.props.searchResult){
            const data = {
                columns : [],
                rows : []
            }
            

            if(this.props.searchResult[0] instanceof Array){
                const dataColumns = this.props.searchResult[0].map(label => {
                    return {
                        label,
                        field : label,
                        width:50
                    }
                });
    
                const dataRows =  this.props.searchResult.slice(1)
                .map((row) => {
                    const tuple = {}
                    
                    row.forEach((value,index) => {
                        if(dataColumns[index] && dataColumns[index].hasOwnProperty('field')){
                            tuple[dataColumns[index].field] = value
                        }
                    });
                    return tuple
                })
                
                data.columns = dataColumns;
                data.rows = dataRows;
            }
            else{

                
                var dataColumns = [];
                if(this.props.searchResult.length > 0){
                    dataColumns = Object.keys(this.props.searchResult[0]).map(key => {
                        return {label : key,field : key,width : 50}
                    });
                }

                const dataRows = this.props.searchResult;

                
                data.columns = dataColumns;
                data.rows = dataRows;
            }


            
            return (
                <DataTable data={data} />
            )
            
        }

        if(this.props.quickSearch){
            // console.log(this.props.quickSearch, this.props.stats)
            return (
                <QuickSearch 
                    colors={this.props.quickSearch[1]}
                    clarity={this.props.quickSearch[2]}
                    colorValues={this.props.quickSearch[4]}
                    clarityValues={this.props.quickSearch[5]}
                    caratValues={this.props.quickSearch[6]}
                    stats={this.props.stats}
                />
            )
        }
        if(this.props.text === null){
            return (
                <LoadingSpinner />
            );
        }

        if(this.props.fileAck){
            return (
                <span>
                    {this.props.text}. Click <a href={this.props.downloadURL} target="_blank">here</a>. to download.
                </span>
            )
        }
        return this.props.text.split('\n').map((phrase, index) =>{
            return (
                <span key={index}>
                    {phrase}
                    <br />
                </span>
            )
        })
    }
    render(){
        const {photoUrl, name, text} = this.props;
        return (
            <div class="item py-4 px-2 d-flex ">
                <img class="ui avatar image inline" src={photoUrl} />
                <div class="content w-100">
                    <div class="header p-1">{this.renderChild()}</div>
                    <small class="text-muted small p-1 ">{name}</small>
                </div>
            </div>
        );
    }
}

export default MessageDetail;
