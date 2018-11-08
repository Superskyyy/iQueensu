import React,{Component} from 'react'
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';
import PostData from './data.json'

class PostList extends Component {
    state = {
        activeMarker:{},
        selectedPlace : {},
        showingInfoWindow:false
    };

    onMarkerClick = (props,marker) =>
        this.setState({
            activeMarker: marker,
            selectedPlace: props,
            showingInfoWindow: true
        });
    onInfoWindowClose = () =>
        this.setState({
           activeMarker:null,
           showingInfoWindow:false
        });
    onMapClicked = () => {
    if (this.state.showingInfoWindow)
      this.setState({
        activeMarker: null,
        showingInfoWindow: false
      });
    };
    render () {
        return (
            <Map
                google={this.props.google}
                onClick = {this.onMapClicked}
                initialCenter={{
                 lat: 44.2252795,
                 lng: -76.4973299
      }}
            zoom={15}>
                {PostData.map((dataDetail,index)=>{
                return <Marker key={dataDetail.id}
                    name={dataDetail.name}
                    lat1={dataDetail.lat}
                    lng1={dataDetail.lng}
                    onClick={this.onMarkerClick}
                    position={{lat:this.lat1,lng:this.lng1}}/>
            })}
            <InfoWindow
              marker={this.state.activeMarker}
            onClose={this.onInfoWindowClose}
            visible={this.state.showingInfoWindow}>
            <div>
                <h1>{this.state.selectedPlace.name}</h1>
            </div>
          </InfoWindow>
            </Map>
        )
    }
}

export  default PostList