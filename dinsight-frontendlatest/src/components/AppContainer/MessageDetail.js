
import React from 'react';
import LoadingSpinner from '../util/LoadingSpinner';
import DataTable from './DataTable';
import quickSearch from './quickSearch';
import QuickSearch from './quickSearch';

class MessageDetail extends React.Component{
    renderChild = () => {
        // console.log(this.props)
        if(this.props.searchResult){

            const data = []

            for(const key in this.props.searchResult)data.push(this.props.searchResult[key])

            

            const dataColumns = data[0].map(label => {
                return {
                    label,
                    field : label,
                    width:50
                }
            });
        
            const dataRows =  data.slice(1)
            .map((row) => {
                const tuple = {}
                
                row.forEach((value,index) => {
                    if(dataColumns[index] && dataColumns[index].hasOwnProperty('field')){
                        tuple[dataColumns[index].field] = value
                    }
                });
                return tuple
            })


            return (
                <DataTable data={{
                    columns: dataColumns.filter(item => {
                        if(item.label === 'VideoFullLinks' || item.label === 'Size' || item.label === 'Branch')return false;
                        return true
                    }),
                    rows : dataRows
                }} />
            )
            
        }

        if(this.props.queryMode==='quick-search'){
            
            const quickSearchparsed=JSON.parse(this.props.quickSearch);
            const statsparsed=JSON.parse(this.props.stats);

            return (
                <QuickSearch 
                    colors={quickSearchparsed[1]}
                    clarity={quickSearchparsed[2]}
                    colorValues={quickSearchparsed[4]}
                    clarityValues={quickSearchparsed[5]}
                    caratValues={quickSearchparsed[6]}
                    stats={statsparsed}
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
                    Click <a href={this.props.downloadURL} target="_blank">here</a>. to download.
                </span>
            )
        }
        // return this.props.text.split('\n').map((phrase, index) =>{
        //     return (
        //         <span key={index}>
        //             {phrase}
        //             <br />
        //         </span>
        //     )
        // })
        // console.log(this.props.text.split('\\n'))
    }
    render(){
        
        const {photoUrl, name, text} = this.props;
        return (
            <div class="item py-4 px-2 d-flex ">
                <img class="ui avatar image inline" src={photoUrl} />
                <div class="content w-100">
                    <div class="header p-1">
                        {
                            this.props.queryMode === 'help'?
                            text.split('\\n').map((phrase, index) =>{
                                return (
                                    <span key={index}>
                                        <pre>{phrase}</pre>
                                    </span>
                                )
                            }):
                            text.split('\\n').map((phrase, index) =>{
                                return (
                                    <span key={index}>
                                        {phrase}
                                        <br />
                                    </span>
                                )
                            })
                        }
                    </div>
                    <div class="header p-1">
                        {this.renderChild()}
                    </div>
                    <small class="text-muted small p-1 ">{name}</small>
                </div>
            </div>
        );
    }
}

export default MessageDetail;
