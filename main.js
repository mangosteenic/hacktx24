import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
renderer.setAnimationLoop( animate );
document.body.appendChild( renderer.domElement );

camera.position.set(-4, 3, 7);
camera.lookAt(0, 2.5, 0);

const loader = new GLTFLoader();

loader.load( '/arcade_machine/scene.gltf', function ( gltf ) {

	gltf.scene.scale.set(0.01, 0.01, 0.01);
    scene.add(gltf.scene);

}, undefined, function ( error ) {

	console.error( error );

} );

const ambientLight = new THREE.AmbientLight( 0xffffff ); // soft white light
scene.add( ambientLight );

const directionalLight1 = new THREE.DirectionalLight( 0xffffff, 1 );
directionalLight1.position.set(-5, 5, 5);
scene.add( directionalLight1 );

const directionalLight2 = new THREE.DirectionalLight( 0xffffff, 1 );
directionalLight2.position.set(5, 5, 5);
scene.add( directionalLight2 );

const hemisphereLight = new THREE.HemisphereLight( 0xffffff, 0xffffff, 1 );
scene.add( hemisphereLight );

const floorGeometry = new THREE.PlaneGeometry(500, 500); // Large plane
const floorMaterial = new THREE.MeshStandardMaterial({ color: 0x2b2b2b, side: THREE.DoubleSide }); // Material
const floor = new THREE.Mesh(floorGeometry, floorMaterial);
floor.rotation.x = -Math.PI / 2; // Rotate the plane to make it horizontal
floor.position.y = 0; // Position it at y = 0
scene.add(floor);

let targetPosition = new THREE.Vector3();
let isAnimating = false;
let animationProgress = 0;

window.addEventListener('click', () => {
	const start = document.getElementById('start');
	start.style.display = 'none';

	targetPosition.set(0, 3.5, .25);
	animationProgress = 0;
	isAnimating = true;
});

function animate() {
	if (isAnimating) {
		animationProgress += 0.005;
		if (animationProgress >= 1) {
			animationProgress = 1;
			isAnimating = false;
		}

		if (animationProgress >= 0.5) {
			const menu = document.getElementById('menu');
			menu.style.display = 'block';
		}

		camera.position.lerpVectors(camera.position, targetPosition, animationProgress);
		camera.lookAt(0, 3.4, 0);
	}

	renderer.render(scene, camera);
}

document.getElementById('yes').addEventListener('click', () => {
	const menuItems = document.querySelectorAll('#menu p, #menu button');
	menuItems.forEach(item => item.style.display = 'none');

	const bot = document.getElementById('bot');
	bot.style.display = 'block';
});
