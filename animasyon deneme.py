import pygame
import time

def enter_animation():
    # Ekran genişliği ve yüksekliği
    WIDTH, HEIGHT = 800, 600

    # Pygame'in başlatılması
    pygame.init()

    # Ekran yüzeyinin oluşturulması
    screen = pygame.display.set_mode ((WIDTH, HEIGHT), pygame.FULLSCREEN)

    # YOUos metninin fontu ve boyutu
    font = pygame.font.Font (None, 100)

    # Metin yüzeyinin ve dikdörtgenin oluşturulması
    text_surface = font.render ("YOUos", True, (255, 255, 255))
    text_rect = text_surface.get_rect (center=(WIDTH // 2, HEIGHT // 2))

    # Animasyon süresi (saniye cinsinden)
    animation_duration = 10

    # Animasyonun başlama zamanı
    start_time = time.time ()

    # Ana döngü
    running = True
    while running :
        # Kullanıcıdan gelen olayları kontrol etme
        for event in pygame.event.get () :
            if event.type == pygame.QUIT :
                running = False

        # Ekranı siyah renkle temizleme
        screen.fill ((0, 0, 0))

        # Animasyon süresi hesaplama
        current_time = time.time ()
        elapsed_time = current_time - start_time

        # Metni hareket ettirme
        text_rect.y = int (HEIGHT / 2 + (elapsed_time / animation_duration) * HEIGHT / 2)

        # Metni ekrana çizme
        screen.blit (text_surface, text_rect)

        # Ekranı güncelleme
        pygame.display.flip ()

        # Animasyonun tamamlanmasını kontrol etme
        if elapsed_time >= animation_duration :
            running = False

    # Pygame'i kapatma
    pygame.quit ()

