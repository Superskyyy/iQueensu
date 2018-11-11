import React, {Component} from 'react'
import './App.css'
import PostData from './postdata.json'
import HouseList from './HouseList'
import logo from './rsz_blood.png'

class MainMap extends Component {

    state = {
        locations: []
    }

    componentDidMount() {
        this.renderMap()
    }

    renderMap = () => {
        loadScript("https://maps.googleapis.com/maps/api/js?" +
            "key=AIzaSyApYnvaIs_OrTPauFoYfNpX149PhTJ_u44&callback=initMap")
        window.initMap = this.initMap
    }


    //Create a map
    initMap = () => {
        var map = new window.google.maps.Map(document.getElementById('map'), {
            center: {lat: 44.2252795, lng: -76.4973299},
            zoom: 15
        })

        //Create an Info window
        var infowindow = new window.google.maps.InfoWindow()

        //set state to json data
        this.setState({
            locations: PostData
        })

        console.log(this.state.location)

        // map json data to markers and info window
        this.state.locations.map(location => {

            var contentString = location.name
            var marker = new window.google.maps.Marker({
                position: {lat: location.lat, lng: location.lng},
                map: map,
                title: location.name
            })

            //when click on a marker, display info window
            marker.addListener('click', function () {

                //change the content
                infowindow.setContent(contentString)

                //open an infowindow
                infowindow.open(map, marker)

            })

        })


    }


    render() {
        return (
            <main>
                <div id="map">
                </div>
                <div id="houseList">
                    <h1> house list</h1>
                    <HouseList name = {PostData.map((data) =>{
                        return(
                            <div>{data.name}</div>
                        )
                    })}/>
                </div>
            </main>
        )
    }
}

function loadScript(url) {
    var index = window.document.getElementsByTagName("script")[0]
    var script = window.document.createElement("script")
    script.src = url
    script.async = true
    script.defer = true
    index.parentNode.insertBefore(script, index)
}


export default MainMap