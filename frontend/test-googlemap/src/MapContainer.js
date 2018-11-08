import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';
import React from 'react';

export class MapContainer extends React.Component {
  render() {
    return (
      <Map google={this.props.google} zoom={15}
        initialCenter={{
            lat: 44.2252795,
            lng: -76.4973299
      }}>
        
      </Map>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: ('AIzaSyApYnvaIs_OrTPauFoYfNpX149PhTJ_u44')
})(MapContainer)