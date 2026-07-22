
document.addEventListener('DOMContentLoaded', function() {

        // ===== 1. REVEAL ON SCROLL =====
        const revealElements = document.querySelectorAll('.reveal-left, .reveal-right, .reveal-card');

        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -40px 0px'
        });

        revealElements.forEach(el => revealObserver.observe(el));

        // ===== 2. TYPEWRITER EFFECT =====
        const typewriterElement = document.getElementById('typewriterText');
        if (typewriterElement) {
            const phrases = [
                'Precision brass engineering for Zimbabwe',
                'Industrial valves & fittings you can trust',
                'Manufacturing excellence since 2018',
                'Built for durability. Engineered for performance.'
            ];
            let phraseIndex = 0;
            let charIndex = 0;
            let isDeleting = false;
            let typeSpeed = 60;

            function typeEffect() {
                const currentPhrase = phrases[phraseIndex];
                if (!isDeleting) {
                    // Typing
                    typewriterElement.textContent = currentPhrase.substring(0, charIndex + 1);
                    charIndex++;
                    if (charIndex === currentPhrase.length) {
                        isDeleting = true;
                        setTimeout(typeEffect, 2500);
                        return;
                    }
                    setTimeout(typeEffect, typeSpeed + Math.random() * 30);
                } else {
                    // Deleting
                    typewriterElement.textContent = currentPhrase.substring(0, charIndex - 1);
                    charIndex--;
                    if (charIndex === 0) {
                        isDeleting = false;
                        phraseIndex = (phraseIndex + 1) % phrases.length;
                        setTimeout(typeEffect, 400);
                        return;
                    }
                    setTimeout(typeEffect, typeSpeed * 0.5);
                }
            }

            // Start typewriter after a short delay
            setTimeout(typeEffect, 800);
        }

        // ===== 3. COUNTER ANIMATION =====
        const counters = document.querySelectorAll('.counter');
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = parseInt(entry.target.closest('.stat-item').dataset.count) || 0;
                    animateCounter(entry.target, target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(c => counterObserver.observe(c));

        function animateCounter(element, target) {
            let current = 0;
            const increment = Math.ceil(target / 60);
            const duration = 1800;
            const stepTime = Math.floor(duration / 60);

            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                element.textContent = current.toLocaleString();
            }, stepTime);
        }

        // ===== 4. RIPPLE EFFECT ON BUTTONS =====
        document.querySelectorAll('.btn-ripple').forEach(btn => {
            btn.addEventListener('click', function(e) {
                const rect = this.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const ripple = document.createElement('span');
                ripple.className = 'ripple-effect';
                ripple.style.left = x + 'px';
                ripple.style.top = y + 'px';
                ripple.style.width = '20px';
                ripple.style.height = '20px';
                this.appendChild(ripple);
                setTimeout(() => ripple.remove(), 700);
            });
        });

        // ===== 5. PARTICLES BACKGROUND =====
        const particlesContainer = document.getElementById('heroParticles');
        if (particlesContainer) {
            for (let i = 0; i < 25; i++) {
                const particle = document.createElement('span');
                const size = 2 + Math.random() * 6;
                particle.style.width = size + 'px';
                particle.style.height = size + 'px';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.top = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 18 + 's';
                particle.style.animationDuration = (14 + Math.random() * 20) + 's';
                particle.style.opacity = 0.04 + Math.random() * 0.08;
                particlesContainer.appendChild(particle);
            }
        }

        // ===== 6. SMOOTH SCROLL FOR INDICATOR =====
        const scrollIndicator = document.getElementById('scrollIndicator');
        if (scrollIndicator) {
            scrollIndicator.addEventListener('click', function() {
                const featuresSection = document.getElementById('featuresSection');
                if (featuresSection) {
                    featuresSection.scrollIntoView({ behavior: 'smooth' });
                }
            });
        }

        // ===== 7. PARALLAX ON HERO IMAGE =====
        const heroImage = document.querySelector('.hero-image-card');
        if (heroImage) {
            document.addEventListener('mousemove', function(e) {
                const rect = heroImage.getBoundingClientRect();
                const x = (e.clientX - rect.left) / rect.width - 0.5;
                const y = (e.clientY - rect.top) / rect.height - 0.5;
                const rotateY = x * 4;
                const rotateX = -y * 4;
                heroImage.style.transform =
                    `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px)`;
            });

            heroImage.addEventListener('mouseleave', function() {
                heroImage.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg) translateY(0)';
                heroImage.style.transition = 'transform 0.6s ease';
                setTimeout(() => {
                    heroImage.style.transition = '';
                }, 600);
            });
        }

        // ===== 8. FEATURE CARDS STAGGER =====
        const featureCards = document.querySelectorAll('.feature-card');
        featureCards.forEach((card, index) => {
            const delay = parseInt(card.dataset.delay) || index * 100;
            card.style.transitionDelay = delay + 'ms';
        });

        console.log('🚀 NFC Industrial — Enhanced experience loaded.');
    });

