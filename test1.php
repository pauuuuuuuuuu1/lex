<!-- announcements for the current month -->
<?php
    // Assuming you have already established a database connection ($dbh)

    $currentMonth = date('Y-m');

    $stmt = $dbh->prepare("SELECT id, title, content, image_path, created_at FROM announcements WHERE DATE_FORMAT(created_at, '%Y-%m') = :currentMonth ORDER BY created_at DESC");
    $stmt->bindParam(':currentMonth', $currentMonth, PDO::PARAM_STR);
    $stmt->execute();

    $announcements = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<section class="previous-announcements section" id="previous-announcements">
    <h2 class="section__title-1">
        <span>Previous Announcements</span>
    </h2>

    <div id="carouselExampleCaptions" class="carousel slide">
        <div class="carousel-inner">
            <?php foreach ($announcements as $index => $announcement): ?>
                <div class="carousel-item <?php echo ($index === 0) ? 'active' : ''; ?>">
                    <img src="<?php echo $announcement['image_path']; ?>" class="d-block w-100" alt="Announcement Images" data-bs-toggle="modal" data-bs-target="#modal-<?php echo $announcement['id']; ?>">
                    <div class="carousel-caption d-md-block">
                        <h5><?php echo $announcement['title']; ?></h5>
                        <p><?php echo date('F j, Y', strtotime($announcement['created_at'])); ?></p>
                    </div>
                </div>

                <!-- Modal for Full Announcement -->
                <div class="modal fade" id="modal-<?php echo $announcement['id']; ?>" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog custom-modal">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLabel" style="font-weight:bold;"><?php echo htmlspecialchars($announcement['title']); ?></h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <!-- Display the image if available -->
                                <?php if (!empty($announcement['image_path'])): ?>
                                    <div style="text-align: center;">
                                        <img src="<?php echo $announcement['image_path']; ?>" class="img-fluid" style="max-height: 500px; max-width:600px; margin-bottom: 20px;">
                                    </div>
                                <?php endif; ?>
                                <!-- Format and display the content in the modal -->
                                <p class="card-text" style="text-align: justify;"><?php echo formatContent($announcement['content'], 90000); ?></p>
                            </div>
                        </div>
                    </div>
                </div>
            <?php endforeach; ?>
        </div>

        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</section>

<?php
function formatContent($content, $previewLength = 70) {
    // Replace line breaks with HTML line breaks
    $formattedContent = nl2br($content);

    // Truncate content to show a preview
    $preview = substr($formattedContent, 0, $previewLength);
    if (strlen($formattedContent) > $previewLength) {
        $preview .= '...';
    }

    return $preview;
}
?>


  <!-- /* Custom styles for carousel */
     #announcements {
            text-align: center;
        }

        .carousel {
            max-width: 600px; /* Adjust the maximum width as needed */
            margin: 0 auto; /* Center the carousel horizontally */
        }

        .carousel-inner {
            border-radius: 10px; /* Add rounded corners to the caro -->