import React,{Component} from 'react'
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';
import PostData from './data';

export class MapContainer extends Component {
  render() {
    return (
      <Map
                google={this.props.google}
                onClick = {this.onMapClicked}
                initialCenter={{
                 lat: 44.2252795,
                 lng: -76.4973299
      }}
            zoom={15}>

export default GoogleApiWrapper({
  apiKey: ("AIzaSyApYnvaIs_OrTPauFoYfNpX149PhTJ_u44")
})(MapContainer)