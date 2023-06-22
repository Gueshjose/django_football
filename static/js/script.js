import * as THREE from 'https://unpkg.com/three@0.126.1/build/three.module.js';
import {OrbitControls} from 'https://unpkg.com/three@0.126.1/examples/jsm/controls/OrbitControls.js'
import { OBJLoader } from 'https://unpkg.com/three@0.126.1//examples/jsm/loaders/OBJLoader'
import { MTLLoader } from 'https://unpkg.com/three@0.126.1//examples/jsm/loaders/MTLLoader'

function init() {
    const canvas = document.querySelector('canvas.webgl')

    // create a scene, that will hold all our elements such as objects, cameras and lights.
    const scene = new THREE.Scene();

    /****
    *  Models
    */

    const mtlLoader = new MTLLoader();
    mtlLoader.load('http://127.0.0.1:8000//static/models/Soccer_Arena_Large_03.mtl', function (materials) {
        materials.preload();

        const objLoader = new OBJLoader();
        objLoader.setMaterials(materials);
        objLoader.load('http://127.0.0.1:8000/static/models/Soccer_Arena_Large_03.obj', function (object) {
            object.position.x=0
            object.position.y=0
            object.position.z=0
            scene.add(object);
        });
    });
    
    
    
    
    

    /**
     * Lights
     */
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.8)
    ambientLight.position.set(5, 10, 25)
    scene.add(ambientLight)
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.6)
    directionalLight.shadow.mapSize.set(1024, 1024)
    directionalLight.shadow.camera.far = 15
    directionalLight.shadow.camera.left = - 7
    directionalLight.shadow.camera.top = 7
    directionalLight.shadow.camera.right = 7
    directionalLight.shadow.camera.bottom = - 7
    directionalLight.position.set(5, 5, 5)
    scene.add(directionalLight)

    // create a camera, which defines where we're looking at
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    // tell the camera where to look
    camera.position.set(10, 1, 10);
    camera.updateMatrixWorld();
    camera.lookAt(0, 20, -30);
    // create a render and set the size
    const sizes = {
        width: window.innerWidth,
        height: window.innerHeight,
    }

    const controls = new OrbitControls(camera, canvas)
    controls.enableDamping = false
    controls.dampingFactor = 0.01; // Facteur d'amortissement
    controls.autoRotate = true; // Activer la rotation automatique
    controls.autoRotateSpeed = 0.3; // Vitesse de rotation automatique
    controls.enableRotate = false; // Désactiver la rotation avec la souris
    controls.enableZoom = false; // Désactiver le zoom avec la souris
    controls.enablePan = false; // Désactiver le déplacement avec la souris

    const renderer = new THREE.WebGLRenderer({canvas: canvas});
    renderer.setSize(sizes.width, sizes.height);
    // function for re-rendering/animating the scene
    function tick() {
        requestAnimationFrame(tick);
        controls.update();
        renderer.render(scene, camera);
    }
    tick();
}
init();