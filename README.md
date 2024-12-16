# Generative Adversarial Networks

Generative Adversarial Networks (GANs) are an innovative class of machine learning models where two neural networks compete against each other in a zero-sum game. Developed by Ian Goodfellow and colleagues in 2014, GANs revolutionized the field of deep learning, especially in synthetic data generation.

The basic operation of a GAN involves two main networks:
- The Generator (G): Responsible for creating synthetic data trying to mimic real data
- The Discriminator (D): Tries to distinguish between real and artificially generated data

This adversarial dynamic allows GANs to learn to generate extremely realistic data, with applications in:
- Photorealistic image generation
- Domain translation (e.g., photo to painting)
- Video and audio synthesis
- Data generation for dataset augmentation
- Design and artistic content creation

GANs represent one of the most significant advances in generative AI of the last decade, opening extraordinary possibilities for creating artificial content indistinguishable from real content.

This repo contains the code for the Generative Adversarial Networks course from Coursera.
Link to the course: [link](https://www.coursera.org/learn/generative-adversarial-networks-gans)

## Course 1: Generative Adversarial Networks (GANs)

In this course, students will:
- Learn about GANs and their applications
- Understand the intuition behind the fundamental components of GANs
- Explore and implement multiple GAN architectures
- Build conditional GANs capable of generating examples from determined categories

## Course 2: Generative Adversarial Networks (GANs)

In this course, students will:
- Assess the challenges of evaluating GANs and compare different generative models
- Use the Fréchet Inception Distance (FID) method to evaluate the fidelity and diversity of GANs
- Identify sources of bias and the ways to detect it in GANs
- Learn and implement the techniques associated with the state-of-the-art StyleGANs


## Course 3: Generative Adversarial Networks (GANs)

In this course, students will:

- Explore the applications of GANs and examine them wrt data augmentation, privacy, and anonymity
- Leverage the image-to-image translation framework and identify applications to modalities beyond images
- Implement Pix2Pix, a paired image-to-image translation GAN, to adapt satellite images into map routes (and vice versa)
- Compare paired image-to-image translation to unpaired image-to-image translation and identify how their key difference necessitates different GAN architectures
- Implement CycleGAN, an unpaired image-to-image translation model, to adapt horses to zebras (and vice versa) with two GANs in one
