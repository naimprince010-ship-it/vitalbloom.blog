import Image from "next/image";

type PostImageProps = {
  alt: string;
  className?: string;
  imageUrl: string;
  priority?: boolean;
};

export default function PostImage({
  alt,
  className = "",
  imageUrl,
  priority = false
}: PostImageProps) {
  if (!imageUrl) {
    return null;
  }

  return (
    <Image
      src={imageUrl}
      alt={alt}
      width={1600}
      height={900}
      className={className}
      priority={priority}
      sizes="(min-width: 1024px) 768px, (min-width: 640px) 90vw, 100vw"
    />
  );
}
