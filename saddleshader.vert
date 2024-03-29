#version 330
// saddleshader.vert

//////////////// Inputs to shader ////////////////
// Uniforms:
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

// Vertex buffers:
in vec2 texCoord;
in vec4 position;
in vec4 normal;

////////////////////////////////////////////////

// Interpolated attributes:
out vec4 fragmentPosition;
out vec4 fragmentNormal;
out vec2 fragmentTexCoord;
out vec4 eye;

void main()
{
    fragmentTexCoord = texCoord;
    mat4 mvMatrix = viewMatrix * modelMatrix;
    fragmentNormal = mvMatrix * normal;
    fragmentPosition = mvMatrix * position;
    eye = -normalize(vec4(fragmentPosition.xyz, 0.0));

    // Magic variable to tell OpenGL where the vertex is:
    gl_Position = projectionMatrix * fragmentPosition;   
}
