Summary:	Metacity window manager configuration program
Summary(pl):	Program konfiguracyjny dla mened�era okien Metacity
Name:		metacity-setup
Version:	0.6.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://plastercast.tzo.com/~plastercast/Projects/%{name}-%{version}.tar.gz
URL:		http://plastercast.tzo.com/~plastercast/Projects/
BuildRequires:	GConf2-devel >= 1.2.0
BuildRequires:	gnome-vfs2-devel >= 2.0.1
BuildRequires:	gtk+2-devel >= 2.0.5 
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	metacity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix  /usr/X11R6

%description
metacity-setup is simply a much easier way to configure Metacity then
having to use gconftool or gconf-editor. It allows you to change
themes, focus settings, and the number of workspaces.

%description -l pl
U�ycie metacity-setup jest du�o prostszym sposobem na skonfigurowanie
Metacity ni� u�ywanie gconftoola lub gconf-editora. metacity-setup
pozwala na zmian� motyw�w, ustawie� focusa i liczby ekran�w
wirtualnych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/metacity-setup-icon.png
%dir %{_datadir}/metacity-setup
%dir %{_datadir}/metacity-setup/pixmaps
%{_datadir}/metacity-setup/pixmaps/metacity-setup-icon.png
%{_datadir}/control-center-2.0/capplets/metacity-setup.desktop
